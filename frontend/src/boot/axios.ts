import axios from 'axios';

const api = axios.create({ baseURL: process.env.API, timeout: 10000 });

export { api };
