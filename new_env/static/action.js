
document.addEventListener("DOMContentLoaded", () => {
    let button1 = document.querySelector(".button-1");
    button1.addEventListener('click', (e) => {
        e.preventDefault();
        let inputVal = document.getElementById("input-1").value;
        console.log(inputVal)
        console.log("clicked")
        fetch(`/cibil_score/${inputVal}`)
            .then(response => response.json())
            .then(
                data => {
                    if (data.result == false) {
                        alert("Not Eligible For loan as cibil score is too low")
                    } else {
                        let div2 = document.getElementById("showDetail")
                        div2.classList.remove("show")
                    }
                }
            );
    });

    let button2 = document.querySelector('.button-2');
    button2.addEventListener('click', (e) => {
        e.preventDefault();
        //console.log("hello")
        let api_data = []
        api_data[0] = (document.getElementById("input-2").value);
        api_data[1] = (document.getElementById("input-3").value);
        api_data[2] = (document.getElementById("input-4").value);
        api_data[3] = (document.getElementById("input-5").value);
        api_data[4] = (document.getElementById("input-6").value);
        //console.log(api_data)
        fetch(`/details/${api_data.join(',')}`)
            .then(res => res.json())
            .then(data => {
                console.log(data)
                let loanshow = document.getElementById("loan-amount")
                loanshow.textContent = "Loan amount that can be granted ="+data.result;
            });
    })

})

   // .then(data => console.log(data))


