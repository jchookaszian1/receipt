let inputElement = document.getElementById('customFile');
let inputLabel= document.getElementById('formLabel');
console.log(inputElement)
inputElement.onchange = () => {
    const selectedFile = inputElement.files[0];
    var data = new FormData()
    data.append('files', selectedFile) // maybe it should be '{target}_cand'
    data.append('name', selectedFile.name)
    const requestOptions = {
        mode: "no-cors",
        method: "POST",
        body: data
    };
    console.log(requestOptions);

    fetch("http://localhost:5000/upload", requestOptions).then(
        (response) => {
            console.log(response.data);
        }
    );
    console.log("hi")
}