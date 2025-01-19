const fetchEmails = async () => {
    const response = await fetch('http://127.0.0.1:5000/get-emails');
    const emails = await response.json();

    console.log('Emails', emails)
};

fetchEmails();