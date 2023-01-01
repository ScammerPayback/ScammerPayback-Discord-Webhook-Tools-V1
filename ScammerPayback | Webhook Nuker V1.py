import requests

# Set the background color and text color
print("\033[44m")

# Print the program title
print("Scammer Payback")

# Set up the base URL for the Discord API
BASE_URL = "https://discordapp.com/api/webhooks"

# Define a function to send a webhook
def send_webhook(webhook_url, num_messages, message):
  # Send the webhook num_messages times
  for i in range(num_messages):
    # Send the webhook message
    requests.post(webhook_url, json={"content": message})

# Define a function to delete a webhook
def delete_webhook(webhook_url):
  # Send a delete request to the webhook URL
  requests.delete(webhook_url)
  print("Webhook deleted.")

# Define a function to get webhook info
def get_webhook_info(webhook_url):
  # Send a get request to the webhook URL
  response = requests.get(webhook_url)
  # Print the webhook information
  print("Webhook information:")
  print(response.json())

# Run the program indefinitely
while True:
  # Print the menu
  print("\nMenu:")
  print("1. Send webhook")
  print("2. Delete webhook")
  print("3. Get webhook info")
  print("4. Close program")

  # Get the user's input
  choice = input("Enter a number: ")

  # Check the user's choice
  if choice == "1":
    # Get the webhook URL
    webhook_url = input("Enter the webhook URL: ")
    # Get the number of messages to send
    num_messages = int(input("Enter the number of messages to send: "))
    # Get the message to send
    message = input("Enter the message to send: ")
    # Send the webhook
    send_webhook(webhook_url, num_messages, message)
  elif choice == "2":
    # Get the webhook URL
    webhook_url = input("Enter the webhook URL: ")
    # Delete the webhook
    delete_webhook(webhook_url)
  elif choice == "3":
    # Get the webhook URL
    webhook_url = input("Enter the webhook URL: ")
    # Get the webhook info
    get_webhook_info(webhook_url)
  elif choice == "4":
    # Close the program
    break
  else:
    print("Invalid choice.")
