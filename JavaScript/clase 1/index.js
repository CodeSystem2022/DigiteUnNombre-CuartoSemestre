const shopContent = document.getElementById ("shopContent");

productos.forEach(product => {
    const content = document.createElement("div");
    <img src ="${product.img}">
        <h3>${product.productName}</h3>
<p>${product.price} $</p>
';
shopContent.append(content);
});