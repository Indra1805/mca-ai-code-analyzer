                           +----------------------+
                           |        User          |
                           +----------------------+
                           | id                  |
                           | username            |
                           | email               |
                           | created_at          |
                           | updated_at          |
                           +----------------------+
                           | __str__()           |
                           +----------+----------+
                                      |
                                      |
                                      | 1
                                      |
                                      |
                                      *
                    +------------------------------------+
                    |      AnalysisHistory               |
                    +------------------------------------+
                    | language                           |
                    | source_code                        |
                    | detected_errors                    |
                    | explanation                        |
                    | corrected_code                     |
                    | best_practices                     |
                    | raw_response                       |
                    | confidence_score                   |
                    | report_download_count              |
                    | analysis_duration_ms               |
                    | analysis_status                    |
                    | created_at                         |
                    | updated_at                         |
                    +------------------------------------+
                    | __str__()                          |
                    +------------------------------------+