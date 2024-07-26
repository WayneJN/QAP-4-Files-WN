// Software Development - SD12
// QAP 4 - Project 3 - JavaScript
// Date : July 26this, 2024
// Submitted by : Wayne Norman



// Program starts here
// Add object to pull information from later
function Customer(firstName, lastName, birthDate, gender, roomPreferences, paymentMethod, mailingAddress, phoneNumber, checkInDate, checkOutDate) {
    this.name = `${firstName} ${lastName}`;
    this.birthDate = new Date(birthDate);
    this.gender = gender;
    this.roomPreferences = roomPreferences;
    this.paymentMethod = paymentMethod;
    this.mailingAddress = mailingAddress;
    this.phoneNumber = phoneNumber;
    this.checkInDate = new Date(checkInDate);
    this.checkOutDate = new Date(checkOutDate);

//Function to calculate the age of the user in years
    this.getAge = function() {
        let today = new Date();
        let age = today.getFullYear() - this.birthDate.getFullYear();
        let m = today.getMonth() - this.birthDate.getMonth();
        if (m < 0 || (m === 0 && today.getDate() < this.birthDate.getDate())) {
            age--;
        }
        return age;
    };

//Function to calculate duration of the visit in days
    this.getDurationOfStay = function() {
        let diffTime = Math.abs(this.checkOutDate - this.checkInDate);
        let diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); 
        return diffDays;
    };

//Dynamic script to display all aquired data and display in paragraph
    this.getDescription = function() {
        return `A new customer, ${this.name}, born on ${this.birthDate.toDateString()} is interested in booking a room at the grand Motel. They are currently ${this.getAge()} years old, and have a gender preference of ${this.gender}. Their preferred mode of contact is by phone, and the primary number is ${this.phoneNumber}. They will be travelling all the way from ${this.mailingAddress.street}, ${this.mailingAddress.city}, ${this.mailingAddress.province},${this.mailingAddress.country} ${this.mailingAddress.postalCode}. They will be checking in on ${this.checkInDate.toDateString()} and checking out on ${this.checkOutDate.toDateString()}.  The duration of their visit will be ${this.getDurationOfStay()} days. Room preferences will include ${this.roomPreferences.join(', ')} and will be paying via ${this.paymentMethod}. 
        `;
    };
}


//Assign the information taken from the submission form
document.getElementById('customerForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    // Prevent the form from being submitted normally
    let firstName = document.getElementById('firstName').value;
    let lastName = document.getElementById('lastName').value;
    let birthDate = document.getElementById('birthDate').value;
    let gender = document.getElementById('gender').value;
    
    // Get all checkboxes
    let checkboxes = document.getElementsByName('roomPreferences');
    let roomPreferences = [];
    for (let i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            roomPreferences.push(checkboxes[i].value);
        }
    }

    let paymentMethod = document.getElementById('paymentMethod').value;
    
    // Get mailing address details
    let mailingAddressStreet = document.getElementById('mailingAddressStreet').value;
    let mailingAddressCity = document.getElementById('mailingAddressCity').value;
    let mailingAddressPostalCode = document.getElementById('mailingAddressPostalCode').value;
    let mailingAddressProvince = document.getElementById('mailingAddressProvince').value;
    let mailingAddressCountry = document.getElementById('mailingAddressCountry').value;
    let mailingAddress = {
        street: mailingAddressStreet,
        city: mailingAddressCity,
        postalCode: mailingAddressPostalCode,
        province: mailingAddressProvince,
        country: mailingAddressCountry
    };

    let phoneNumber = document.getElementById('phoneNumber').value;
    let checkInDate = document.getElementById('checkInDate').value;
    let checkOutDate = document.getElementById('checkOutDate').value;

    let customer = new Customer(firstName, lastName, birthDate, gender, roomPreferences, paymentMethod, mailingAddress, phoneNumber, checkInDate, checkOutDate);
    console.log(customer.getDescription());



    // Have the paragraph from the console appear on the HTML page
    let p = document.createElement('p');
    // Set the innerHTML of the paragraph to the customer description
    p.innerHTML = customer.getDescription();
    // Append the paragraph to the body of the document
    document.body.appendChild(p);
});


