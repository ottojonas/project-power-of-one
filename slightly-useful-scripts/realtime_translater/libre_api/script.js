const startBtn = document.getElementById("start_button");
const translatedText = document.getElementById("translated_text");

const SpeechRecog = window.SpeechRecog || window.webkitSpeechRecognition;
const recognition = new SpeechRecog();

recognition.lang = "es-ES";

recognition.onresult = async (event) => {
  const speechResult = event.results[0][0].transcript;
  console.log("speech recognised:", speechResult);

  const translated = await translateText(speechResult, "en");
  translatedText.textContent = translated;
};
recognition.onerror = (event) => {
  console.error("error:", event.error);
};

startBtn.addEventListener("click", () => {
  recognition.start();
});


async function translateText(text, targetLang) {
    try {
      const response = await fetch(`https://libretranslate.com/translate`, {
        method: "POST",
        body: JSON.stringify({
          q: text,
          source: "es",
          target: targetLang,
          format: "text",
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      return data.translatedText;
    } catch (error) {
      console.error("Network error:", error);
      return "Translation failed";
    }
  }