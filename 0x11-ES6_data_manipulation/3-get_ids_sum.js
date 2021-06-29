export default function getStudentIdsSum(students) {
  if (Array.isArray(students) === false) {
    return 0;
  }
  const getId = (sum, j) => sum + j.id;
  return students.reduce(getId, 0);
}
