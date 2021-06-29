export default function updateStudentGradeByCity(students, city, newGrades) {
  /* eslint-disable no-param-reassign */
  if (Array.isArray(students) === false) {
    return [];
  }
  return students.filter((y) => y.location === city).map((y) => {
    y.grade = 'N/A';
    for (const gr of newGrades) {
      if (gr.studentId === y.id) {
        y.grade = gr.grade;
      }
    }
    return y;
  });
}
