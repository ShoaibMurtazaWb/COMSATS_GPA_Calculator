

import streamlit as st

grade_points_map = {
    'A': 4.00,
    'A-': 3.66,
    'B+': 3.33,
    'B': 3.00,
    'B-': 2.60,
    'C+': 2.33,
    'C': 2.00,
    'C-': 1.66,
    'D+': 1.30,
    'D': 1.00,
    'F': 0.00
}

st.title("🎓 GPA / CGPA Calculator")

mode = st.radio("Choose one:", ["Semester GPA", "CGPA"])

# ------------------ Semester GPA ------------------
if mode == "Semester GPA":
    st.subheader("Semester GPA")

    number_of_courses = st.number_input(
        "Number of courses", min_value=1, max_value=50, value=4, step=1
    )

    total_credit_hours = 0.0
    total_grade_points = 0.0

    for course_index in range(1, number_of_courses + 1):
        st.write("**Course", course_index, "**")

        credit_hours = st.number_input(
            f"Credit hours (Course {course_index})",
            min_value=0.0,
            value=3.0,
            step=0.5,
            key=f"credit_{course_index}"
        )

        grade_letter = st.selectbox(
            f"Letter grade (Course {course_index})",
            options=list(grade_points_map.keys()),
            index=3,
            key=f"grade_{course_index}"
        )

        if credit_hours > 0:
            grade_point_value = grade_points_map[grade_letter]
            total_credit_hours = total_credit_hours + credit_hours
            total_grade_points = total_grade_points + (credit_hours * grade_point_value)

        st.divider()

    if st.button("Calculate Semester GPA"):
        if total_credit_hours > 0:
            semester_gpa = total_grade_points / total_credit_hours
            semester_gpa = round(semester_gpa, 2)
            st.success(f"Your Semester GPA: {semester_gpa}")
            st.write("Total Credit Hours:", round(total_credit_hours, 2))
            st.write("Total Grade Points (Σ credits × points):", round(total_grade_points, 2))
        else:
            st.error("Please enter at least one course with credit hours > 0.")

# ------------------ CGPA ------------------
if mode == "CGPA":
    st.subheader("Cumulative GPA (CGPA)")

    number_of_semesters = st.number_input(
        "Number of semesters", min_value=1, max_value=50, value=2, step=1
    )

    total_semester_credits = 0.0
    total_weighted_points = 0.0

    for semester_index in range(1, number_of_semesters + 1):
        st.write("**Semester", semester_index, "**")

        semester_credit_hours = st.number_input(
            f"Total credit hours (Semester {semester_index})",
            min_value=0.0,
            value=15.0,
            step=0.5,
            key=f"sem_credit_{semester_index}"
        )

        semester_gpa = st.number_input(
            f"GPA (Semester {semester_index})",
            min_value=0.0,
            max_value=4.0,
            value=3.0,
            step=0.01,
            key=f"sem_gpa_{semester_index}"
        )

        if semester_credit_hours > 0:
            total_semester_credits = total_semester_credits + semester_credit_hours
            total_weighted_points = total_weighted_points + (semester_credit_hours * semester_gpa)

        st.divider()

    if st.button("Calculate CGPA"):
        if total_semester_credits > 0:
            cumulative_gpa = total_weighted_points / total_semester_credits
            cumulative_gpa = round(cumulative_gpa, 2)
            st.success(f"Your CGPA: {cumulative_gpa}")
            st.write("Total Credits (All Semesters):", round(total_semester_credits, 2))
            st.write("Total Weighted Points (Σ credits × GPA):", round(total_weighted_points, 2))
        else:
            st.error("Please enter at least one semester with credit hours > 0.")
