import requests, json


#The following are objects that will be utilized in the program: 
def showdata(data):
  temp = data['main']['temp']
  hightemp = data['main']['temp_max']
  print('Current Temperature : {} degrees fahrenheit'.format(temp))
  print('High Temperature : {} degrees fahrenheit'.format(hightemp))
def by_city():
  city = int(input("Please enter the city you would like to search."))
  url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=f058cf8dc1d6aa586cdd7e335743a14b&units=imperial'.format(city)
  res = requests.get(url)
  data = res.json()
  showdata(data)
  question = input('Would you like to try again? Type Yes or No: ')
  if question == 'Yes' or question == 'yes':
        main()
  if question == 'No' or question == 'no':
        print("Thank you and stay dry!")
        exit()
def by_zip():
  zip = int(input("Please enter the zip code you would like to search."))
  url = "https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=f058cf8dc1d6aa586cdd7e335743a14b".format(zip)
  res = requests.get(url)
  data = res.json()
  showdata(data)
  question = input('Would you like to try again? Type Yes or No: ')
  if question == 'Yes' or question == 'yes':
        main()
  if question == 'No' or question == 'no':
        print("Thank you and stay dry!")
        exit()

def main():
  while True:
    answer = input("How would you like to search? \nType City for a City.\nType Zip to search by Zip Code\n")
    if answer == "City" or answer == "city":
      try:
        by_city()
      except Exception:
        print("That didn't work. Please try again.")
        by_city()
    if answer == "Zip" or answer == "zip":
      try:
        by_zip()
      except Exception:
        print("That didn't work. Please try again.")
      by_zip()
  else:
    print("Sorry, that did not work, please try again.")
main()