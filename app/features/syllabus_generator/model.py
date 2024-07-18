from pydantic import BaseModel, Field
from typing import List, Dict


class SyllabusModel(BaseModel):
    title: str = Field(description="The title for the whole course")
    overview: str = Field(
        description="A broad overview of what is expected of students and what they will learn"
    )
    objectives: List[str] = Field(
        description="A list of specific tasks the student will be able to successfully do upon completion of the course",
        examples=[
            [
                "Define the key terms associated with electrocardiographs.",
                "Describe the cardiac cycle and the conduction systems that controls the cardiac cycle.",
                "Describe the electrocardiogram.",
            ],
            [
                "Craft short plays with clear action, developed characters, and precise dialogue",
                "Apply feedback to your own writing through revision",
                "Analyse and discuss the craft of contemporary plays",
            ],
        ],
    )

    policies_and_exceptions: Dict[str, str] = Field(
        description="Class policies, exceptions, important rules and any special consideration all students must be aware of. Each has a title and contents.",
        examples=[
            {
                "performance_expectations": {
                    "mastery_of_subject_matter": "Students are expected to demonstrate a mastery of the subject matter covered in the course.",
                    "critical_analysis": "Students are expected to be able to critically analyze scientific information and arguments.",
                    "research_skills": "Students are expected to be able to conduct research and use scientific literature to support their work.",
                    "professional_behavior": "Students are expected to behave in a professional manner at all times.",
                },
                "feedback_and_improvement": {
                    "feedback_process": "Students will receive feedback on their work through written comments, discussion, and peer review.",
                    "options_for_grade_improvement": "Students may have the opportunity to improve their grades by resubmitting assignments or completing additional work.",
                },
                "communication": {
                    "grades_and_feedback": "Grades and feedback will be communicated to students through the online course management system and in person during office hours.",
                    "academic_advising": "Students may also meet with their academic advisor to discuss their grades and progress in the course.",
                },
                "special_considerations": {
                    "accommodations_for_students_with_disabilities": "Students with disabilities who need accommodations should contact the Disability Services office.",
                    "academic_support_resources": "Students may also access a variety of academic support resources, such as tutoring, writing centers, and counseling services.",
                },
            },
        ],
    )

    grade_level_assessments: Dict[str, Dict[str, int | str]] = Field(
        description="assessment components and grade scale for completing the course. Assessment components being a dictionary of components and percentages, grade_scale being a dictionary of grades and percentage ranges",
        examples=[
            {
                "assessment_components": {
                    "assignments": 20,
                    "exams": 25,
                    "projects": 25,
                    "presentations": 15,
                    "participation": 15,
                },
                "grade_scale": {
                    "A": "90-100%",
                    "B": "80-89%",
                    "C": "70-79%",
                    "D": "60-69%",
                    "F": "Below 60%",
                },
            },
        ],
    )

    # This can be expanded

    model_config = {
        "json_schema_extra": {
            "examples": """
            {
                "title": "ELECTROCARDIOGRAPH TECHNIQUE & APPLICATION",
                "overview": "Acquiring a deeper understanding of the cardiovascular system and how it functions, students
                    practice basic electrocardiograph patient care techniques, applying legal and ethical responsibilities. Students learn the
                    use of medical instrumentation, electrocardiogram theory, identification of and response to mechanical problems,
                    recognition of cardiac rhythm and response to emergency findings.",
                "objectives": [
                        "Define the key terms associated with electrocardiographs.",
                        "Describe the cardiac cycle and the conduction systems that controls the cardiac cycle.",
                        "Describe the electrocardiogram.",
                        "Maintain equipment for safety and accuracy; identify and eliminate or report interference and
                        mechanical problems."
                    ],
                "policies_and_exceptions": {
                    "attendance requirements":
                        "It is important for the school to be notified when a student is not able to attend class. It is the student’s responsibility to
                        inquire about make-up work for both classroom lectures and laboratory sessions.
                        Tardiness and/or absence from any part of a class/lab will constitute a partial absence. A total of three partial absences
                        will constitute a full absence. ",
                    "make-up work":
                        "It is the student’s responsibility to inquire about make-up work for both classroom and laboratory sessions. The
                        instructor will not re-teach material, therefore there is no charge for make-up work. For information regarding make-up
                        work."
                },
                "grade_level_assessments": {
                    "assessment_components": {
                        "assignments": 20,
                        "exams": 25,
                        "projects": 25,
                        "presentations": 15,
                        "participation": 15,
                    },
                    "grade_scale": {
                        "A": "90-100%",
                        "B": "80-89%",
                        "C": "70-79%",
                        "D": "60-69%",
                        "F": "Below 60%",
                    }
            }
            """
        }
    }