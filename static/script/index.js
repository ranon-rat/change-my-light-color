const color = document.getElementById("color");
const [rInput, gInput, bInput] = [
  document.getElementById("red"),
  document.getElementById("green"),
  document.getElementById("blue"),
];

const submit = document.getElementById("submit");

function componentToHex(c) {
  var hex = c.toString(16);
  return hex.length == 1 ? "0" + hex : hex;
}

function rgbToHex(r, g, b) {
  return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}

function hexToRgb(hex) {
  return {
    red: parseInt(hex.slice(1, 3), 16),
    green: parseInt(hex.slice(3, 5), 16),
    blue: parseInt(hex.slice(5, 7), 16),
  };
}
function changeColor() {
  const [r, g, b] = [rInput, gInput, bInput].map((input) =>
    parseInt(input.value)
  );
  console.log(r, g, b);
  color.value = rgbToHex(r, g, b);
}
color.addEventListener("change", function () {
  const rgbColor = hexToRgb(this.value);
  [rInput, gInput, bInput].forEach((input) => {
    input.value = rgbColor[input.id];
  });
});
submit.onclick = () => {
  fetch("/color", {
    method: "POST",
    body: color.value,
  });
};
[rInput, gInput, bInput].forEach((input) => {
  input.addEventListener("change", function () {
    color.value = rgbToHex(
      ...[rInput, gInput, bInput].map((input) => parseInt(input.value))
    );
  });
});
