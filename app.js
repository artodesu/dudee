const express = require('express');
const app = express();
const PORT = 3000;

function fibonacci(n) {
    const sequence = [0, 1];
    for (let i = 2; i < n; i++) {
        sequence.push(sequence[i - 1] + sequence[i - 2]);
    }
    return sequence;
}

app.get('/api/v1/test/:count', (req, res) => {
    const memberCount = parseInt(req.params.count);

    if (isNaN(memberCount) || memberCount < 1 || memberCount > 100) {
        return res.status(400).json({ error: 'Invalid member count. Please provide a number between 1 and 100.' });
    }

    const sequence = fibonacci(memberCount);
    const total = sequence.reduce((acc, val) => acc + val, 0);

    res.json({
        'member-count': memberCount,
        'sequence': sequence,
        'total': total
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
