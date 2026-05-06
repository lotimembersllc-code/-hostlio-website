export default async function handler(req, res) {
  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Authorization, Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  const token = req.headers['authorization'];

  if (!token) {
    return res.status(401).json({ error: 'Token gerekli' });
  }

  const BASE_ID = 'appPFfJ4ljiG0qjTq';
  const TABLE_ID = 'tbllyzYyAtA6bfD65';

  try {
    let allRecords = [];
    let offset = null;

    do {
      let url = `https://api.airtable.com/v0/${BASE_ID}/${TABLE_ID}?pageSize=100`;
      if (offset) url += `&offset=${offset}`;

      const response = await fetch(url, {
        headers: { 'Authorization': token }
      });

      if (!response.ok) {
        const err = await response.text();
        return res.status(response.status).json({ error: err });
      }

      const data = await response.json();
      allRecords = allRecords.concat(data.records || []);
      offset = data.offset;
    } while (offset);

    return res.status(200).json({ records: allRecords });

  } catch (err) {
    return res.status(500).json({ error: err.message });
  }
}
