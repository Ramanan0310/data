(function () {
  "use strict";

  function showAlert(message, type) {
    const container = document.querySelector(".container");
    if (!container) return;

    const existing = container.querySelector(".alert");
    if (existing) existing.remove();

    const alert = document.createElement("div");
    alert.className = "alert alert-" + type;
    alert.setAttribute("role", "alert");
    alert.textContent = message;
    container.insertBefore(alert, container.firstChild);

    window.setTimeout(function () {
      alert.remove();
    }, 4000);
  }

  function validateMobile(value) {
    const cleaned = value.replace(/[\s\-()]/g, "");
    return /^\+?[0-9]{7,15}$/.test(cleaned);
  }

  function validateForm(data) {
    if (!data.part_number || !data.blo_name || !data.blo_designation || !data.blo_mobile) {
      return "All fields are required.";
    }
    if (!validateMobile(data.blo_mobile)) {
      return "Enter a valid mobile number (7–15 digits).";
    }
    return null;
  }

  const form = document.getElementById("entry-form");
  if (!form) return;

  form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const submitBtn = form.querySelector('button[type="submit"]');
    const payload = {
      part_number: form.part_number.value.trim(),
      blo_name: form.blo_name.value.trim(),
      blo_designation: form.blo_designation.value.trim(),
      blo_mobile: form.blo_mobile.value.trim(),
    };

    const error = validateForm(payload);
    if (error) {
      showAlert(error, "error");
      return;
    }

    submitBtn.disabled = true;
    submitBtn.textContent = "Saving…";

    try {
      const response = await fetch("/api/save", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const result = await response.json();

      if (!response.ok || !result.success) {
        throw new Error(result.message || "Failed to save record.");
      }

      form.reset();
      form.part_number.focus();
      showAlert(result.message || "Record saved successfully.", "success");
    } catch (err) {
      showAlert(err.message || "Failed to save record.", "error");
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = "Save to SQL Server";
    }
  });
})();
