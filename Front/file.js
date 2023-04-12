

async function getMusic() {
    const res = await fetch('http://192.168.0.103:8000/api/answers/noise', );
    var mus = await res.json();
    mus = mus["Audio"]

    console.log(mus);
    mus.forEach(mu => musToHTML(mu));
}

window.addEventListener('DOMContentLoaded', getMusic);

function musToHTML({pk, audio}) {
    const musList = document.getElementById(`blocks`);
    console.log(audio)
    musList.insertAdjacentHTML('beforeend', `
        <div class="bl_1">
            <audio controls="controls" class = "audio1">
                <source src = "http://192.168.0.103:8000${audio}" type ="audio/mpeg">
                <a href="http://192.168.0.103:8000${audio}">
                    Download audio
                </a>
            </audio>
            <form class="feedback" name="feedback">
                <div class="form_ans">Что вы слышали?</div>
                <div class = "butform">
                    <input id="idForm_${pk}" type="text" class="form-control" placeholder="Введите ответ">
                    <button id="addform_${pk}" type="submit" class="but">Отправить</button>
                </div>
            </form>
        </div>

    `)
    const but = document.getElementById(`addform_${pk}`)
    but.addEventListener('click', async () => {
        const input = document.getElementById(`idForm_${pk}`)
        const title = input.value;
        console.log("POST")
        if (title) {
            const res = await fetch('http://192.168.0.103:8000/api/answers/noise/create', {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json'
                },
                body: JSON.stringify({audioNoise: `${pk}`, text: `${title}`, availability: true})
            });
    
            const mus = await res.json();
        }
    })

}

