function addToCart(name, price) {
    fetch(`/add_to_cart/${name}/${price}`)
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function checkout() {
    fetch('/checkout')
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            document.getElementById('cart-items').innerHTML = '';
            document.getElementById('cart-total').textContent = '0.00';
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
