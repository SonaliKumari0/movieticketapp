🎟️ Movie Ticket Booking App
A full-featured Django-based web application that allows users to browse movies, select theaters, choose showtimes, book tickets, make secure payments, and write reviews. This project integrates multiple Django apps to deliver a seamless and dynamic movie ticket booking experience.

🌐 Live Demo
🔗 movieticketapp-fual.onrender.com

🔧 Features
User Authentication (Login, Signup, Logout)

Movie Listings with dynamic details

Theater and Show Management

Real-time Seat Selection and Booking

Secure Payments Integration

Booking History Dashboard

Movie Reviews and Ratings

Admin Panel for Managing Content

🛠️ Tech Stack
Backend: Django, Django REST Framework

Frontend: HTML5, CSS3, Bootstrap

Database: SQLite (for development)

Deployment: Render

Other Tools: Stripe (for payments), Django Allauth, Crispy Forms

📁 Project Structure (Modules)
accounts – User registration and authentication

bookings – Seat booking and ticket management

dashboard – User dashboard to view booking history

movies – Movie listings and detail pages

reviews – User-generated reviews and ratings

theater – Theater and showtime management

payments – Integration of payment gateway

static & templates – Static files and HTML templates

📌 How to Run Locally
Clone the repository

Create and activate a virtual environment

Install dependencies using pip install -r requirements.txt

Configure .env variables

Run python manage.py migrate and python manage.py runserver

📢 Contribution
Open to contributions! Feel free to fork the repo, raise issues, or submit pull requests.
