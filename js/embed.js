import EmbedJS from "embed-js"; // install by npm i -S embed-js@beta
import basic from "embed-preset-basic";

import "./index.css";

// This uses the basic preset which contains a collection of plugins.
// You can also use all the plugins separately.
var x = new EmbedJS({
  input: document.getElementById("rootElem"),
  preset: basic({
    gAuthKey: "AIzaSyCqFouT8h5DKAbxlrTZmjXEmNBjC69f0ts",
    facebook: {
      height: 460
    },
    exclude: ["youtube"]
  })
});


x.render();

// The below code is only for toggling the apply and destroy methods.
let isEmbedApplied = true;

document.getElementById("button").onclick = function toggle(a) {
  if (isEmbedApplied) {
    this.innerText = "Apply embed-js";
    x.destroy();
  } else {
    this.innerText = "Destroy";
    x.render();
  }
  isEmbedApplied = !isEmbedApplied;
};
