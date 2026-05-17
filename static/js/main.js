const message = document.getElementById("msgs")
function removeMsg(event) {
  const button = event.target;
  const parent = button.parentElement;
  parent.remove();
}