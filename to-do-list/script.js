console.log("JS is linked!");

// Select elements
const input = document.querySelector(".input-container input");
const addBtn = document.querySelector(".input-container button");
const taskList = document.querySelector(".task-list");

// Function to add a new task
function addTask() {
  const taskText = input.value.trim(); // get text from input

  if (taskText === "") return; // ignore empty input

  // Create li element
  const li = document.createElement("li");

  // Create checkbox
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";

  // Create span (task text)
  const span = document.createElement("span");
  span.textContent = taskText;

  // Create delete button
  const deleteBtn = document.createElement("button");
  deleteBtn.textContent = "x";
  deleteBtn.classList.add("delete");

  // Add delete functionality
  deleteBtn.addEventListener("click", () => {
    li.remove();
  });

  // Append elements to li
  li.appendChild(checkbox);
  li.appendChild(span);
  li.appendChild(deleteBtn);

  // Add li to task list
  taskList.appendChild(li);

  // Clear input
  input.value = "";
}

// Add task when button is clicked
addBtn.addEventListener("click", addTask);