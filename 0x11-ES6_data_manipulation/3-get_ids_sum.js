export default function getStudentIdsSum(students) {
  if (Array.isArray(students) === false) {
    return 0;
  }
  let red = (sum, s) => sum + s.id;
  return students.reduce(red, 0);
}
