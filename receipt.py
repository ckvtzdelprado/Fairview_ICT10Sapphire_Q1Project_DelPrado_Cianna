from pyscript import document


def generate_receipt(event):

    products = document.querySelectorAll(".product")


    subtotal = 0


    for product in products:
        if product.checked:
            price = float(product.value)
            subtotal = subtotal + price


    vat = subtotal * 0.12


    total = subtotal + vat


    if subtotal == 0:
        document.getElementById("receipt").innerText = (
            "Please select at least one product."
        )
        return


    receipt = "PAWFECT PETS\n\n"
    receipt = receipt + "Subtotal: ₱" + str(subtotal) + "\n"
    receipt = receipt + "VAT (12%): ₱" + str(vat) + "\n"
    receipt = receipt + "Total Amount: ₱" + str(total)


    document.getElementById("receipt").innerText = receipt