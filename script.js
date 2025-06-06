// Simple module database
const modules = {
  stopTheBleed: {
    title: "Stop the Bleed",
    progress: 0,
    questions: [
      {
        question: "What is the first step in controlling life-threatening bleeding?",
        answers: ["Apply tourniquet", "Recognize bleeding", "Pack wound"],
        correct: "Recognize bleeding"
      },
      {
        question: "What tool is used to stop severe bleeding from a limb?",
        answers: ["Tourniquet", "Sling", "Ice pack"],
        correct: "Tourniquet"
      },
      {
        question: "Where should a tourniquet be applied?",
        answers: ["Above the wound", "Directly on the wound", "Below the wound"],
        correct: "Above the wound"
      },
      {
        question: "How tight should a tourniquet be?",
        answers: [
          "Tight enough to stop bleeding",
          "Loose for comfort",
          "Just snug"
        ],
        correct: "Tight enough to stop bleeding"
      },
      {
        question: "When should you pack a wound?",
        answers: [
          "When direct pressure fails to control bleeding",
          "Before applying pressure",
          "If a bandage is unavailable"
        ],
        correct: "When direct pressure fails to control bleeding"
      },
      // ... continue adding up to 25 questions
    ],
  },
  runHideFight: {
    title: "Active Assailant: Run, Hide, Fight",
    progress: 0,
    questions: [
      {
        question: "What is your first action if you hear gunfire?",
        answers: ["Run if safe", "Call 911", "Hide immediately"],
        correct: "Run if safe"
      },
      {
        question: "Where is the best place to hide?",
        answers: [
          "Behind locked doors and out of sight",
          "In an open hallway",
          "Next to large windows"
        ],
        correct: "Behind locked doors and out of sight"
      },
      {
        question: "When should you fight an assailant?",
        answers: [
          "Only as a last resort",
          "Immediately",
          "Never fight"
        ],
        correct: "Only as a last resort"
      },
      {
        question: "What is a key tactic while running?",
        answers: [
          "Zigzagging to make yourself harder to hit",
          "Running in a straight line",
          "Calling 911 while running"
        ],
        correct: "Zigzagging to make yourself harder to hit"
      },
      {
        question: "When hiding, what is important?",
        answers: [
          "Turn off lights and silence your phone",
          "Yell for help",
          "Make noise to scare the attacker"
        ],
        correct: "Turn off lights and silence your phone"
      },
      // ... continue adding up to 25 questions
    ],
  }
};

// Launch selected module
function startModule(moduleKey) {
  const module = modules[moduleKey];
  if (!module) return;

  // Update progress
  module.progress = 100;
  localStorage.setItem(moduleKey, "completed");
  alert(`You have completed ${module.title}!`);
  renderDashboard();
}

// Render dashboard
function renderDashboard() {
  const progressDiv = document.getElementById("progress");
  progressDiv.innerHTML = "";

  Object.keys(modules).forEach((key) => {
    const module = modules[key];
    const status = localStorage.getItem(key) === "completed" ? "Completed" : "Not Started";

    const moduleStatus = document.createElement("div");
    moduleStatus.innerHTML = `
      <h3>${module.title}</h3>
      <p>Status: <strong>${status}</strong></p>
    `;

    progressDiv.appendChild(moduleStatus);
  });
}

// On page load
window.onload = function () {
  renderDashboard();
};
