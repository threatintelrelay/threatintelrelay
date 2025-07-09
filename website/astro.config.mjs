// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
               starlight({
                       title: 'ThreatIntelRelay',
                       social: [
                               { icon: 'github', label: 'GitHub', href: 'https://github.com/threatintelrelay/threatintelrelay' },
                       ],
                       sidebar: [
                               {
                                       label: 'Guides',
                                       items: [
                                               { label: 'Quickstart', slug: 'guides/quickstart' },
                                               { label: 'Example Guide', slug: 'guides/example' },
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
