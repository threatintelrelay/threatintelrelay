// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';



// https://astro.build/config
export default defineConfig({
	integrations: [
               starlight({
                       title: 'Threat Intel Relay',
                       social: [
                               { icon: 'github', label: 'GitHub', href: 'https://github.com/threatintelrelay/threatintelrelay' },
                       ],
                       sidebar: [
                               {
                                       label: 'Users',
                                       items: [
                                               { label: 'Example Guide', slug: 'user_guides/example' },
                                       ],
                               },
                                {
                                        label: 'Developers',
                                        items: [
                                                { label: 'Quickstart', slug: 'dev_guides/quickstart' },
                                                { label: 'Dev Security Tools', slug: 'dev_guides/security_tools' },
                                        ],
                                },
                               {
                                       label: 'Reference',
                                       autogenerate: { directory: 'reference' },
                               },
                       ],
               }),
	],
});
