const modalContainer = document.getElementById("modal-container");
const modalOverlay = document.getElementById("modal-overlay");

cosnt cartBtn = document.getElementById("cart-btn");
const displayCart = () =>{

    modalContainer.innerHTML = "";

    modalContainer.style.display = "block";
    modalOverlay.style.display = "block";

cosnt modalHeader = document.createElement("div");

const modalClose = document.createElement("div");
modalClose.innerText = "📌"
modalClose.className = "Modal"
modalHeader.append(modalClose)

modalClose.addEventListener("Click", ()=> {
    modalContainer.style.display = "none";
    modalOverlay.style.display = "none";
});

const modalTitle = document.createElement("div");

modalTitle.innerText = "cart";
modalTitle.className = "modal-title";
modalHeader.append(modalTitle);

modalContainer.append(modalHeader);

};

cartBtn.addEventListener("click",displayCart);
