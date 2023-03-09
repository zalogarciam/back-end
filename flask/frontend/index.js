const studentsFetch = async () => {
  const result = await fetch("http://localhost:5000/students", {
    method: "GET",
  });

  const data = await result.json();
  console.log(data);
};

document.addEventListener("DOMContentLoaded", function () {
  studentsFetch();
});
