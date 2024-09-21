
fetch(`/verfügbareGeräte`)
    .then((resp)=>resp.json())
    .then((data)=>{
        const geraeteListe = document.getElementById("geraeteListe");
        geraeteListe.innerText ="";
        data.forEach(element => {
            const Zeile = document.createElement("li")
            Zeile.innerHTML = `<span id="Bezeichnung">Bezeichnung: ${element[0]}</span>   <span id="Produktgruppe">Produktgruppe: ${element[1]}</span>`
            geraeteListe.appendChild(Zeile)
        });
        
    })
.catch(error => console.error('Error fetching data:', error));