const startBtn = document.getElementById('start-btn')
const translatedText = document.getElementById('translated-text')

const SpeechRecog = window.SpeechRecog || window.webkitSpeechRecognition
const recognition = new SpeechRecog(); 

recognition.lang = 'es-ES'

recognition.onresult = async (event) => {
    const speechResult = event.results[0][0].transcript; 
    console.log('speech recognised:', speechResult);

    const translated = await translatedText(speechResult, 'en')
    translatedText.textContent = translated 
}
recognition.onerror = (event) => {
    console.error('error:', event.error)
}

startBtn.addEventListener('click', () => {
    recognition.start(); 
})

async function translateText(text, targetLang) {
    const response = await fetch(`https://translation.googleapis.com/language/translate/v2?key=YOUR_API_KEY`, {
        method: 'POST', 
        body: JSON.stringify({
            q:text, 
            target: targetLang
        }), 
        headers: {
            'Content-Type': 'application/json'
        }
    })
    const data = await response.json()
    return data.data.translations[0].translateText
}