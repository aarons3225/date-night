# date-night
An at home date night generator that has food recommendations based on movies.

https://github.com/user-attachments/assets/9f42fdce-b53c-4aa5-be3f-d01f31eae03b

# Requirements
- docker
- python3
  
# Install

In a terminal navigate to a folder where you can clone this repo, or stay in the home folder. Then use this command:

```
git clone https://github.com/aarons3225/date-night.git
```

Go into that folder:
```
cd date-night
```

Build the container:
```
sudo docker compose build
```

Test the app:
```
sudo docker compose up
```
to end the running proccess, ctrl + "c".

Run the app as a daemon:
```
docker compose up -d
```
