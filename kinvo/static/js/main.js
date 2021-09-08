// Enroll process
const newsForm = document.getElementById("news");

newsForm.addEventListener("submit", (event) => {
  const content = document.getElementById("content");
  content.innerHTML = "";

  const modal = document.getElementById("lock-modal");
  const loading = document.getElementById("loading");

  // stop form submission
  event.preventDefault();

  // lock down the form
  modal.style.visibility = "visible";
  loading.style.visibility = "visible";

  axios
    .post("/api/v1/news")
    .then((response) => showNews(response))
    .catch((error) => {
      alert(error);
      console.log(error);
    })
    .then(() => {
      modal.style.visibility = "hidden";
      loading.style.visibility = "hidden";
    });
});

function showNews(response) {
  const content = document.getElementById("content");

  // creates a <table> element and a <tbody> element
  const tbl = document.createElement("table");
  const tblHead = document.createElement("thead");

  tblHead.innerHTML = `<tr><th> Titles (<i class="fas fa-link fa-xs"></i>) </th><th> Published on </th></tr>`;
  tbl.appendChild(tblHead);

  const tblBody = document.createElement("tbody");

  response.data.forEach(function (el) {
    let row = document.createElement("tr");
    let link = document.createElement("a");
    let cellTitle = document.createElement("td");
    let cellPub = document.createElement("td");

    const title = document.createTextNode(`${el.title}`);
    const date = moment(el.pubdate).locale("pt-br").format("DD/MM/YYYY");

    let icon = document.createElement("i");
    icon.className = "fas fa-link";

    link.appendChild(title);
    link.appendChild(icon);
    link.href = `${el.url}`;

    cellTitle.appendChild(link);
    cellPub.appendChild(document.createTextNode(`${date}`));

    row.appendChild(cellTitle);
    row.appendChild(cellPub);

    row.className = "tr-dynamic";

    tblBody.appendChild(row);
  });

  tbl.appendChild(tblBody);

  content.appendChild(document.createElement("p").appendChild(tbl));
}

// Entities process
const entitiesForm = document.getElementById("entities");

entitiesForm.addEventListener("submit", (event) => {
  const content = document.getElementById("content");
  content.innerHTML = "";

  const modal = document.getElementById("lock-modal");
  const loading = document.getElementById("loading");

  // stop form submission
  event.preventDefault();

  // lock down the form
  modal.style.visibility = "visible";
  loading.style.visibility = "visible";

  axios
    .get("/api/v1/entities")
    .then((response) => showEntities(response))
    .catch((error) => {
      alert(error);
      console.log(error);
    })
    .then(() => {
      modal.style.visibility = "hidden";
      loading.style.visibility = "hidden";
    });
});

function showEntities(response) {
  const content = document.getElementById("content");

  // creates a <table> element and a <tbody> element
  const tbl = document.createElement("table");
  const tblHead = document.createElement("thead");

  tblHead.innerHTML = `<tr><th> Links </th><th> Entities found </th></tr>`;
  tbl.appendChild(tblHead);

  const tblBody = document.createElement("tbody");

  response.data.forEach(function (el) {
    let cellURL = document.createElement("td");

    let link = document.createElement("a");

    let icon = document.createElement("i");
    icon.className = "fas fa-link";

    link.appendChild(icon);
    link.href = `${el.url}`;

    cellURL.appendChild(link);

    let cellEntities = document.createElement("td");

    let entities = el.entities.map((e) => `${e.entity} (${e.label})`);
    entities = `${entities.join([(separador = ", ")])}`;

    cellEntities.appendChild(document.createTextNode(entities));

    let row = document.createElement("tr");

    row.appendChild(cellURL);
    row.appendChild(cellEntities);

    tblBody.appendChild(row);
  });

  tbl.appendChild(tblBody);

  content.appendChild(document.createElement("p").appendChild(tbl));
}
