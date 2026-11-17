// TASK 1 - BILL SPLITTER

document.getElementById("splitButton").onclick = function() {
    // Get values from the input boxes
    var bill = Number(document.getElementById("billAmount").value);
    var tipRate = Number(document.getElementById("tipRate").value);
    var people = Number(document.getElementById("people").value);

    var error = document.getElementById("billError");
    var result = document.getElementById("billResult");

    error.innerHTML = "";
    result.innerHTML = "";

    // Check whether the values are valid
    if (document.getElementById("billAmount").value === "" || bill <= 0) {
        error.innerHTML = "Please enter a valid bill amount.";
        return;
    }

    if (document.getElementById("people").value === "" || people <= 0 || !Number.isInteger(people)) {
        error.innerHTML = "Please enter a valid whole number of people.";
        return;
    }

    // Calculate tip and total
    var tip = bill * tipRate / 100;
    var total = bill + tip;
    var eachPerson = total / people;

    result.innerHTML =
        "Bill amount: Rs. " + bill.toFixed(2) + "<br>" +
        "Tip amount: Rs. " + tip.toFixed(2) + "<br>" +
        "Total with tip: Rs. " + total.toFixed(2) + "<br>" +
        "Each person pays: Rs. " + eachPerson.toFixed(2);
};


// TASK 2 - ADD MENU ITEMS

var totalBill = 0;

document.getElementById("addButton").onclick = function() {
    var name = document.getElementById("itemName").value;
    var priceText = document.getElementById("itemPrice").value;
    var price = Number(priceText);
    var error = document.getElementById("itemError");

    error.innerHTML = "";

    if (name.trim() === "") {
        error.innerHTML = "Please enter the menu item name.";
        return;
    }

    if (priceText === "" || price <= 0) {
        error.innerHTML = "Please enter a valid item price.";
        return;
    }

    // Add the item to the list
    var list = document.getElementById("itemList");
    var newItem = document.createElement("li");
    newItem.innerHTML = name + " - Rs. " + price.toFixed(2);
    list.appendChild(newItem);

    // Add the price to the total
    totalBill = totalBill + price;
    document.getElementById("menuTotal").innerHTML = totalBill.toFixed(2);

    // Clear the input boxes
    document.getElementById("itemName").value = "";
    document.getElementById("itemPrice").value = "";
};


// Split the menu bill
document.getElementById("menuSplitButton").onclick = function() {
    var tipRate = Number(document.getElementById("menuTip").value);
    var peopleText = document.getElementById("menuPeople").value;
    var people = Number(peopleText);
    var error = document.getElementById("menuSplitError");
    var result = document.getElementById("menuResult");

    error.innerHTML = "";
    result.innerHTML = "";

    if (totalBill <= 0) {
        error.innerHTML = "Please add at least one menu item.";
        return;
    }

    if (peopleText === "" || people <= 0 || !Number.isInteger(people)) {
        error.innerHTML = "Please enter a valid whole number of people.";
        return;
    }

    var tip = totalBill * tipRate / 100;
    var total = totalBill + tip;
    var eachPerson = total / people;

    result.innerHTML =
        "Total with tip: Rs. " + total.toFixed(2) + "<br>" +
        "Each person pays: Rs. " + eachPerson.toFixed(2);
};


// TASK 3 - TODO LIST

document.getElementById("todoButton").onclick = function() {
    var task = document.getElementById("todoInput").value;
    var error = document.getElementById("todoError");

    error.innerHTML = "";

    if (task.trim() === "") {
        error.innerHTML = "Please enter a task.";
        return;
    }

    // Create a new list item
    var newTask = document.createElement("li");
    newTask.innerHTML = task;

    // Click the task to mark it as completed
    newTask.onclick = function() {
        newTask.classList.toggle("completed");
    };

    document.getElementById("todoList").appendChild(newTask);

    document.getElementById("todoInput").value = "";
};
