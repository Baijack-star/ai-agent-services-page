document.addEventListener('DOMContentLoaded', function() {
    const button = document.createElement('a');
    button.href = 'booking.html';
    button.className = 'floating-btn bg-purple-600 hover:bg-purple-700 text-white font-bold py-3 px-6 rounded-full text-lg transition duration-300 transform hover:scale-105';
    button.textContent = 'Book Free Consultation';
    document.body.appendChild(button);

    const style = document.createElement('style');
    style.textContent = `
        .floating-btn {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 1000;
        }
    `;
    document.head.appendChild(style);
});
