from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import os
# Replace 'your_bot_token' with your actual bot token
TOKEN = '6418853995:AAFz51kYZK0-UQBB1bB3Dbxhb9RMeq3qIEQ'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Send me an image to upload.")

def handle_image(update, context):
    # Check if the message contains a photo
    print("in handle_image")

    if update.message.photo:
        try:
            # Get the file ID of the image
            file_id = update.message.photo[-1].file_id
            # Get the file path from Telegram servers
            file_path = context.bot.get_file(file_id).file_path
            print(file_path)
            # Download the image file
            image_url= file_path
            url = image_url
            filename = str(update.effective_chat.id)+ '---' + os.path.basename(url)
            print(filename)
            print(image_url)
            image_file = requests.get(image_url)
            image_file.raise_for_status()  # Raise an exception for non-2xx status codes from Telegram API

            # Get image content type (optional, for more accurate content-type)
            content_type = image_file.headers.get('Content-Type', 'image/jpeg')
            if content_type == 'image/png':
                file_extension = 'png'
            else:
                file_extension = 'jpg'

            # Prepare the PUT request
            bucket='cscprojectbucket'
            response = api_url = f'https://umnkot904a.execute-api.us-east-1.amazonaws.com/crcproject/{bucket}/{filename}'  # Replace with your API URL
            print(response)
            files = {'image': (f'image.{file_extension}', image_file.content, content_type)}  # Adjust content type if needed
            try:

                response = requests.put(api_url, data=image_file.content,headers=image_file.headers)
                response.raise_for_status()  # Raise an exception for non-2xx status codes
                # Handle successful upload
                context.bot.send_message(chat_id=update.effective_chat.id, text='Image uploaded successfully!\n Please Wait! The image is getting processed....')
            except requests.exceptions.RequestException as e:
                # Handle errors from API request
                context.bot.send_message(chat_id=update.effective_chat.id, text=f'An error occurred while uploading the image: {e}')
        except Exception as e:  # Catch any other exceptions (e.g., from Telegram API calls)
            context.bot.send_message(chat_id=update.effective_chat.id, text=f'An unexpected error occurred: {e}')
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Please send an image.')


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, handle_image))  # Use Filters.photo instead of filters.PHOTO

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()