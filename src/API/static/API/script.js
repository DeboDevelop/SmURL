document.getElementById("output").placeholder = "http://" + document.domain + ":" + location.port + "/"; 

/**
 * Open the Url in a new tab 
 */
function openNewTab()
{
    let url = document.getElementById("output").value;
    window.open(url);
}

/**
 * Copy the Url into the clipboard
 */
function copyContent()
{
    let copyText = document.getElementById("output");
    copyText.select();
    copyText.setSelectionRange(0, 99999); //For mobile devices
    document.execCommand("copy");
}

/**
 * Post the URL using fetch api or fetch the long_url if it's already exist. 
 */
async function fill()
{
    let input = document.getElementById("input").value
    let response = await fetch('http://127.0.0.1:8000/api/urls')
    let data = await response.json()
    for (let i=0;i<data.length;i++)
    {
        if(data[i].long_url == input)
        {
            document.getElementById("output").value = "http://" + document.domain + ":" + location.port + "/" + data[i].base62_id;
            return;
        }
    }
    let index = data.reverse()[0].id
    let token = encode(index+1)

    let posting = await fetch('http://127.0.0.1:8000/api/urls/', {
        method : "POST",
        body : JSON.stringify({
            id: index+1,
            long_url: input,
            base62_id: token
        }),
        headers: { 
            "Content-type": "application/json; charset=UTF-8"
        } 
    })
    if(posting.ok)
    {
        document.getElementById("output").value = "http://" + document.domain + ":" + location.port + "/" + token; 
    }
    if(posting.status == 400)
    {
        document.getElementById("output").value = "400 Bad Request";
    }
}

/**
 * Encode the Given number into base62
 * @param  {Number} num The number to be encoded.
 */

function encode(num)
{
    if (num === 0) {
        return '0';
    }
    var digits = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    var len = digits.length, base
    var result = ''; 
    while (num > 0) {
        result = digits[num % len] + result;
        num = parseInt(num / len, 10);
    }
    return result;
}