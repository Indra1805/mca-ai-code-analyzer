+--------------------+
|       User         |
+--------------------+
| id (PK)            |
| username           |
| email              |
| password           |
| created_at         |
| updated_at         |
+---------+----------+
          |
          | 1
          |
          | has many
          |
          *
+-------------------------------+
|       AnalysisHistory         |
+-------------------------------+
| id (PK)                       |
| user_id (FK)                  |
| language                      |
| source_code                   |
| detected_errors               |
| explanation                   |
| corrected_code                |
| best_practices                |
| raw_response                  |
| confidence_score              |
| report_download_count         |
| analysis_duration_ms          |
| analysis_status               |
| created_at                    |
| updated_at                    |
+-------------------------------+