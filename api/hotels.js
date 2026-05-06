export default async function handler(req, res) {
  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Authorization, Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  // Token'ı al — hem 'authorization' hem 'Authorization' dene
  const token = req.headers['authorization'] || req.headers['Authorization'];

  if (!token) {
    return res.status(401).json({
      error: 'Token gerekli',
      debug_headers: Object.keys(req.headers)
    });
  }

  // Token "Bearer " ile başlıyorsa aynen gönder, başlamıyorsa ekle
  const authHeader = token.startsWith('Bearer ') ? token : `Bearer ${token}`;

  const BASE_ID = 'appPFfJ4ljiG0qjTq';
  const TABLE_ID = 'tbllyzYyAtA6bfD65';

  try {
    let allRecords = [];
    let offset = null;

    do {
      let url = `https://api.airtable.com/v0/${BASE_ID}/${TABLE_ID}?pageSize=100`;
      if (offset) url += `&offset=${offset}`;

      const response = await fetch(url, {
        headers: { 'Authorization': authHeader }
      });

      if (!response.ok) {
        const err = await response.text();
        return res.status(response.status).json({
          error: err,
          debug_auth_sent: authHeader.substring(0, 20) + '...'
        });
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
