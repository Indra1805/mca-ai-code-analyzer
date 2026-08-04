/*
==========================================================
AI Code Analyzer
Analysis Page JavaScript
==========================================================
*/

document.addEventListener(
    "DOMContentLoaded",
    function () {

        // ==========================================
        // Elements
        // ==========================================

        const sourceCode =
            document.getElementById(
                "sourceCode"
            );

        const analyzeBtn =
            document.getElementById(
                "analyzeBtn"
            );

        const copyBtn =
            document.getElementById(
                "copyBtn"
            );

        const clearBtn =
            document.getElementById(
                "clearBtn"
            );

        const uploadBtn =
            document.getElementById(
                "uploadBtn"
            );

        const characterCount =
            document.getElementById(
                "characterCount"
            );

        const lineCount =
            document.getElementById(
                "lineCount"
            );

        // ==========================================
        // Hidden File Input
        // ==========================================

        const fileInput =
            document.createElement(
                "input"
            );

        fileInput.type = "file";

        fileInput.accept =
            ".py,.java,.c,.cpp,.js,.go,.txt";

        fileInput.style.display =
            "none";

        document.body.appendChild(
            fileInput
        );

        // ==========================================
        // Update Statistics
        // ==========================================

        function updateStatistics() {

            const text =
                sourceCode.value;

            characterCount.textContent =
                text.length;

            if (
                text.length === 0
            ) {

                lineCount.textContent = 0;

            } else {

                lineCount.textContent =
                    text.split("\n").length;

            }

            analyzeBtn.disabled =
                text.trim().length === 0;

        }

        updateStatistics();

        // ==========================================
        // Live Statistics
        // ==========================================

        sourceCode.addEventListener(
            "input",
            updateStatistics
        );

        // ==========================================
        // Copy Code
        // ==========================================

        copyBtn.addEventListener(
            "click",
            async function () {

                if (
                    sourceCode.value.trim() === ""
                ) {

                    alert(
                        "There is no code to copy."
                    );

                    return;

                }

                try {

                    await navigator.clipboard.writeText(
                        sourceCode.value
                    );

                    copyBtn.innerHTML =
                        "Copied ✓";

                    setTimeout(
                        function () {

                            copyBtn.innerHTML =
                                "Copy";

                        },
                        1500
                    );

                } catch {

                    alert(
                        "Unable to copy."
                    );

                }

            }
        );

        // ==========================================
        // Clear Code
        // ==========================================

        clearBtn.addEventListener(
            "click",
            function () {

                const confirmed =
                    confirm(
                        "Clear the editor?"
                    );

                if (
                    !confirmed
                ) {

                    return;

                }

                sourceCode.value = "";

                updateStatistics();

                sourceCode.focus();

            }
        );

        // ==========================================
        // Upload File
        // ==========================================

        uploadBtn.addEventListener(
            "click",
            function () {

                fileInput.click();

            }
        );

        fileInput.addEventListener(
            "change",
            function (event) {

                const file =
                    event.target.files[0];

                if (
                    !file
                ) {

                    return;

                }

                const reader =
                    new FileReader();

                reader.onload =
                    function (e) {

                        sourceCode.value =
                            e.target.result;

                        updateStatistics();

                    };

                reader.readAsText(
                    file
                );

            }
        );

        // ==========================================
        // Tab Support
        // ==========================================

        sourceCode.addEventListener(
            "keydown",
            function (event) {

                if (
                    event.key !== "Tab"
                ) {

                    return;

                }

                event.preventDefault();

                const start =
                    this.selectionStart;

                const end =
                    this.selectionEnd;

                this.value =
                    this.value.substring(
                        0,
                        start
                    ) +
                    "    " +
                    this.value.substring(
                        end
                    );

                this.selectionStart =
                    this.selectionEnd =
                        start + 4;

            }
        );

        // ==========================================
        // Drag & Drop
        // ==========================================

        sourceCode.addEventListener(
            "dragover",
            function (event) {

                event.preventDefault();

            }
        );

        sourceCode.addEventListener(
            "drop",
            function (event) {

                event.preventDefault();

                const file =
                    event.dataTransfer.files[0];

                if (
                    !file
                ) {

                    return;

                }

                const reader =
                    new FileReader();

                reader.onload =
                    function (e) {

                        sourceCode.value =
                            e.target.result;

                        updateStatistics();

                    };

                reader.readAsText(
                    file
                );

            }
        );

        // ==========================================
        // Keyboard Shortcut
        // Ctrl + Enter
        // ==========================================

        sourceCode.addEventListener(
            "keydown",
            function (event) {

                if (
                    event.ctrlKey &&
                    event.key === "Enter"
                ) {

                    document
                        .getElementById(
                            "analysisForm"
                        )
                        .submit();

                }

            }
        );

    }
);