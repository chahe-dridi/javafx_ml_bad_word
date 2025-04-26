module tn.esprit.microservice.test_ml {
    requires javafx.controls;
    requires javafx.fxml;


    opens tn.esprit.microservice.test_ml to javafx.fxml;
    exports tn.esprit.microservice.test_ml;
}