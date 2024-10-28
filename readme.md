Features and Requirements


1. User Authentication:
○ Registration: Implement user registration, allowing new users to create
an account.
○ Login: Implement a login system to authenticate users.
○ Logout: Users should be able to log out.
○ Profile Page: Each user should have a profile page where they can view
and update their personal details. 


2. Event Management:
○ Create Event: A logged-in user can create new events by providing
details such as event name, date, location, and description.
○ Update Event: Users can update their own events.
○ Delete Event: Users can delete events they have posted.
○ View Events: All users (even those not logged in) should be able to
view events on the homepage.
○ Event Permissions: Users can only update or delete events they
created. Admins can manage all events.


3. Event Booking (Logged-In Users Only):
○ Only registered and logged-in users can book an event.
○ Once a user books an event, that event should appear on their Booked
Events page.
○ Display a message on the homepage showing whether the current
logged-in user has already booked a particular event. For example, show
“Booked” next to events that the user has already booked.


4. Homepage:
○ The homepage should display all events.
○ For logged-in users, display the booking status for each event,
indicating if the current user has already booked that event.
○ Non-logged-in users should still be able to see events, but when trying to
book, then redirect the login page.


5. Booked Events Page:
○ Logged-in users should have access to a Booked Events page that lists
all events they have booked.
○ This page should show details of the booked events, such as event name,
date, and location.
6. Navigation and User Experience:
○ Include a navigation bar with links to the homepage, login/logout,
registration, profile, and the user’s booked events page.
7. Features :
○ Search Functionality: Add a search bar to the homepage so users can
search for events by name, date, or location.
○ Event Categories: Implement event categories such as conferences,
concerts, workshops, etc. Allow users to filter events by category.
○ Booking Limits: Set a booking limit for events, so when the event
reaches capacity, it shows “Fully Booked”.


Submission Guidelines:
● Submit the project either as a GitHub repository or a zip file containing the full
Django project with requirement.txt file.
● Ensure the project includes migrations, models, views, templates, and static
files.