from pyscript import document


def generate_sku(event):
    
    category = document.getElementById("category").value
    product = document.getElementById("product").value
    stock = document.getElementById("stock").value

 
    if product == "" or stock == "":
        document.getElementById("result").innerText = (
            "Please enter the product name and stock quantity."
        )
        return

   
    product = product.upper()

    product = product.replace(" ", "")

    product_code = product[:4]


    sku = category + "-" + product_code + "-" + stock


    document.getElementById("result").innerText = sku