const xhr = new XMLHttpRequest()
const method = 'GET'
const url = "/book-list"
const responseType = "json"

xhr.responseType = responseType
xhr.open(method, url)
xhr.onload = function() {
    const serverResponse = xhr.response
    var listedItems = serverResponse.response
    console.log(listedItems)
}
xhr.send()

