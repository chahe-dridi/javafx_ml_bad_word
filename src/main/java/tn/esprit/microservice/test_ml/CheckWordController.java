package tn.esprit.microservice.test_ml;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class CheckWordController {

    @FXML
    private TextField inputField;

    @FXML
    private Label resultLabel;

    @FXML
    protected void onCheckWordClick() {
        String input = inputField.getText().toLowerCase();

        // Call the real model using FastAPI
        String prediction = predictWord(input);

        if ("bad".equalsIgnoreCase(prediction)) {
            resultLabel.setText("⚠️ Bad Word Detected!");
        } else if ("good".equalsIgnoreCase(prediction)) {
            resultLabel.setText("✅ Good Word!");
        } else {
            resultLabel.setText("❓ Error Predicting");
        }
    }

    private String predictWord(String word) {
        try {
            URL url = new URL("http://localhost:8000/predict/");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setDoOutput(true);

            String jsonInputString = "{\"word\":\"" + word + "\"}";
            try(OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonInputString.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

            Scanner scanner = new Scanner(conn.getInputStream());
            String response = scanner.useDelimiter("\\A").next();
            scanner.close();

            // Very simple parsing
            if (response.contains("\"result\":\"bad\"")) {
                return "bad";
            } else if (response.contains("\"result\":\"good\"")) {
                return "good";
            } else {
                return "unknown";
            }

        } catch (Exception e) {
            e.printStackTrace();
            return "error";
        }
    }
}
