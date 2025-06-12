// tailwind.config.js
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    container: {
      padding: {
        DEFAULT: '1rem',
        sm: '2rem',
        lg: '4rem',
        xl: '5rem',
        '2xl': '6rem',
      },
    },
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}