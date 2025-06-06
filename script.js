// Define full training modules
const modules = {
  stopTheBleed: {
    title: "Stop the Bleed",
    progress: 0,
    lessons: [
      "Recognizing life-threatening bleeding.",
      "Applying pressure with hands.",
      "Using tourniquets effectively.",
      "Wound packing with gauze or clean cloth.",
      "Prioritizing safety while administering aid.",
      "Monitoring the victim after control.",
      "Transitioning care to EMS professionals."
    ],
    questions: [
      { question: "What is the first action to control life-threatening bleeding?", answers: ["Apply a tourniquet", "Recognize bleeding", "Pack wound"], correct: "Recognize bleeding" },
      { question: "What tool is critical to stop severe limb bleeding?", answers: ["Tourniquet", "Band-aid", "Sling"], correct: "Tourniquet" },
      { question: "Where should a tourniquet be applied?", answers: ["Above the wound", "On the wound", "Below the wound"], correct: "Above the wound" },
      { question: "How tight must a tourniquet be?", answers: ["Tight enough to stop bleeding", "Loose for comfort", "Snug only"], correct: "Tight enough to stop bleeding" },
      { question: "When should you pack a wound?", answers: ["When direct pressure fails", "Before pressure", "If no tourniquet is available"], correct: "When direct pressure fails" },
      { question: "Bleeding should be controlled within how many minutes if properly treated?", answers: ["5 minutes", "2 minutes", "1 minute"], correct: "5 minutes" },
      { question: "What can you use if a tourniquet is not available?", answers: ["Belt or similar item", "Scarf", "Tape"], correct: "Belt or similar item" },
      { question: "What is the best material for wound packing?", answers: ["Sterile gauze", "Cotton shirt", "Plastic wrap"], correct: "Sterile gauze" },
      { question: "What must you do after applying a tourniquet?", answers: ["Document the time", "Release after 5 minutes", "Massage limb"], correct: "Document the time" },
      { question: "When should you not remove a tourniquet?", answers: ["Until EMS arrives", "After 5 minutes", "After bleeding stops"], correct: "Until EMS arrives" },
    ]
  },
  runHideFight: {
    title: "Active Assailant: Run, Hide, Fight",
    progress: 0,
    lessons: [
      "Develop situational awareness.",
      "Identify exits and escape routes.",
      "Hide effectively and barricade.",
      "Silence devices and stay hidden.",
      "Fight back as a last resort.",
      "Work as a group to survive.",
      "Report accurately to authorities."
    ],
    questions: [
      { question: "What is the first step if you hear gunfire?", answers: ["Run if safe", "Hide immediately", "Fight"], correct: "Run if safe" },
      { question: "Where is the safest hiding spot?", answers: ["Behind locked doors", "In an open hallway", "Near windows"], correct: "Behind locked doors" },
      { question: "When should you fight an assailant?", answers: ["As a last resort", "At first sight", "Never"], correct: "As a last resort" },
      { question: "What is a key tactic while running?", answers: ["Zigzagging", "Running straight", "Shouting"], correct: "Zigzagging" },
      { question: "What should you do when hiding?", answers: ["Turn off lights and silence phones", "Yell for help", "Move constantly"], correct: "Turn off lights and silence phones" },
      { question: "Who should you fight back with?", answers: ["As a team if possible", "Alone only", "Never fight"], correct: "As a team if possible" },
      { question: "What to report to authorities?", answers: ["Location, suspect details", "Only your name", "Stay silent"], correct: "Location, suspect details" },
      { question: "What is a barricade best made of?", answers: ["Heavy furniture", "Curtains", "Boxes"], correct: "Heavy furniture" },
      { question: "What's a last-resort improvised weapon?", answers: ["Fire extinguisher", "Plastic bag", "Shoes"], correct: "Fire extinguisher" },
      { question: "Why silence your phone?", answers: ["Avoid detection", "Save battery", "Distract shooter"], correct: "Avoid detection" },
    ]
  }
};

// Shuffle helper
function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

// Launch module (show lessons first)
function startModule(moduleKey) {
  const module = modules[moduleKey];
  if (!module) return;

  let content = `<h2>${module.title} - Lessons</h2><ol>`;
  module.lessons.forEach(lesson => {
    content += `<li>${lesson}</li>`;
  });
  content += `</ol><br><button onclick="startQuiz('${moduleKey}')">Start Quiz</button>`;

  document.getElementById('modules').innerHTML = content;
}

// Start quiz (after lessons)
function startQuiz(moduleKey) {
  const module = modules[moduleKey];
  if (!module) return;

  const questionsPool = shuffle([...module.questions]).slice(0, 5); // 5 random questions
  let quizContent = `<h2>${module.title} Quiz</h2>`;

  questionsPool.forEach((q, index) => {
    const shuffledAnswers = shuffle([...q.answers]);
    quizContent += `<div><strong>${index + 1}. ${q.question}</strong><br>`;
    shuffledAnswers.forEach(answer => {
      quizContent += `<input type="radio" name="q${index}" value="${answer}"> ${answer}<br>`;
    });
    quizContent += `</div><br>`;
  });

  quizContent += `<button onclick="submitQuiz('${moduleKey}', ${JSON.stringify(questionsPool)})">Submit Quiz</button>`;

  document.getElementById('modules').innerHTML = quizContent;
}

// Submit quiz
function submitQuiz(moduleKey, questionsPool) {
  let score = 0;

  questionsPool.forEach((q, index) => {
    const selected = document.querySelector(`input[name="q${index}"]:checked`);
    if (selected && selected.value === q.correct) {
      score++;
    }
  });

  const percentage = (score / questionsPool.length) * 100;
  if (percentage >= 80) {
    alert(`Congratulations! You passed with ${percentage}%!`);
    modules[moduleKey].progress = 100;
    localStorage.setItem(moduleKey, "completed");
  } else {
    alert(`You scored ${percentage}%. Please try again.`);
    modules[moduleKey].progress = percentage;
    localStorage.setItem(moduleKey, "incomplete");
  }

  renderDashboard();
}

// Render dashboard
function renderDashboard() {
  const progressDiv = document.getElementById("progress");
  progressDiv.innerHTML = "";

  Object.keys(modules).forEach((key) => {
    const module = modules[key];
    const storedProgress = localStorage.getItem(key);
    let status = "Not Started";

    if (storedProgress === "completed") {
      status = "Completed";
    } else if (storedProgress === "incomplete") {
      status = "In Progress";
    }

    const moduleStatus = document.createElement("div");
    moduleStatus.innerHTML = `
      <h3>${module.title}</h3>
      <p>Status: <strong>${status}</strong></p>
    `;

    progressDiv.appendChild(moduleStatus);
  });
}

// Load dashboard on page load
window.onload = function () {
  renderDashboard();
};
