export default function getListStudentIds(objec) {
	if (Array.isArray(objec) === false) {
		return [];
	}
	return objec.map((y) => y.id);
}
