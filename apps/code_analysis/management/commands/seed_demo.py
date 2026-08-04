import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.accounts.models import User
from apps.code_analysis.models import AnalysisHistory


PYTHON_CODE = """
def find_max(numbers):
    maximum = 0

    for num in numbers:
        if num > maximum:
            maximum = num

    return max_value
"""

JAVA_CODE = """
public class Main {

    public static void main(String[] args){

        int total = 100;

        int students = 0;

        System.out.println(total / students);

    }

}
"""

C_CODE = """
#include<stdio.h>

int main(){

    int arr[5]={1,2,3,4,5};

    printf("%d",arr[5]);

    return 0;

}
"""

JS_CODE = """
function calculate(){

let total=100;

console.log(price);

}

calculate();
"""

GO_CODE = """
package main

import "fmt"

func main(){

var numbers []int

fmt.Println(numbers[10])

}
"""

ERRORS = [
    "Undefined variable detected.",
    "Possible runtime exception.",
    "Array index out of bounds.",
    "Division by zero.",
    "Incorrect loop condition.",
    "Variable used before initialization.",
]

BEST_PRACTICES = """
• Use meaningful variable names.
• Validate user inputs.
• Handle exceptions properly.
• Follow language coding standards.
• Write modular code.
"""

EXPLANATION = """
The submitted source code contains programming issues that may lead to compilation or runtime failures. The AI analyzed the program and identified possible causes along with recommendations to improve reliability and readability.
"""


class Command(BaseCommand):

    help = "Populate demo data."

    def handle(self, *args, **kwargs):

        self.stdout.write("Removing previous demo analyses...")

        AnalysisHistory.objects.all().delete()

        users = {
            "indra": User.objects.get(username="indra"),
            "alice": User.objects.get(username="alice"),
            "bob": User.objects.get(username="bob"),
            "charlie": User.objects.get(username="charlie"),
            "david": User.objects.get(username="david"),
        }

        demo_plan = [
            ("indra", "Python", 10, PYTHON_CODE),
            ("indra", "Java", 5, JAVA_CODE),
            ("alice", "Python", 5, PYTHON_CODE),
            ("bob", "Java", 3, JAVA_CODE),
            ("charlie", "C", 6, C_CODE),
            ("david", "JavaScript", 5, JS_CODE),
            ("david", "Go", 4, GO_CODE),
        ]

        for username, language, count, code in demo_plan:

            for _ in range(count):

                created = timezone.now() - timedelta(
                    days=random.randint(0, 30),
                    hours=random.randint(0, 23),
                    minutes=random.randint(0, 59),
                )

                confidence = random.randint(88, 99)

                duration = random.randint(620, 1180)

                status = (
                    AnalysisHistory.AnalysisStatus.SUCCESS
                    if random.random() < 0.92
                    else AnalysisHistory.AnalysisStatus.FAILED
                )

                AnalysisHistory.objects.create(
                    user=users[username],
                    language=language,
                    source_code=code,
                    detected_errors=random.choice(ERRORS),
                    explanation=EXPLANATION,
                    corrected_code=code,
                    best_practices=BEST_PRACTICES,
                    raw_response="Generated for project demonstration.",
                    confidence_score=confidence,
                    report_download_count=random.randint(0, 6),
                    analysis_duration_ms=duration,
                    analysis_status=status,
                    created_at=created,
                )

        self.stdout.write(
            self.style.SUCCESS(
                "Demo data generated successfully."
            )
        )