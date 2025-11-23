const cats = [];
const catSums = [];
const catSumDivs = document.querySelector("#cat-sum-table").querySelectorAll("div");
for (let i = 0; i < catSumDivs.length; i++) {
  if (i % 2 == 0) {
    cats.push(catSumDivs[i].innerText);
  } else {
    catSums.push(Number(catSumDivs[i].innerText.replace("$", "").replace(",", "")));
  }
}

const days = [];
const daySums = [];
const daySumDivs = document.querySelector("#daily-sum-table").querySelectorAll("div");
for (let i = 0; i < daySumDivs.length; i++) {
  if (i % 2 == 0) {
    days.push(daySumDivs[i].innerText);
  } else {
    daySums.push(Number(daySumDivs[i].innerText.replace("$", "").replace(",", "")));
  }
}

let catCtx = document.querySelector("#category-chart").getContext("2d");
let catChart = new Chart(catCtx, {
  type: "pie",
  data: {
    labels: cats,
    datasets: [{
      label: "Expense across categories",
      data: catSums,
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)'
      ],
      borderColor: [
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
      ],
      borderWidth: 1
    }]
  },
  options: {}
})

let dailyCtx = document.querySelector("#daily-chart").getContext("2d");
let dailyChart = new Chart(dailyCtx, {
  type: "line",
  data: {
    labels: days,
    datasets: [{
      label: "Expense across categories",
      data: daySums,
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)'
      ],
      borderColor: [
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
      ],
      borderWidth: 1
    }]
  },
  options: {}
})