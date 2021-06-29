export default function getStudentsByLocation(students, city) {
  if (Array.isArray(students) === false) {
    return [];
  } else {}
  return students.filter((y) => y.location === city);
}
